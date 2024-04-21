from openai import OpenAI
from dotenv import load_dotenv

from ws.ws.spiders.LinkedinSpider import LinkedinScrapperSettings as lss

PROMPT_MAIL_GENERATION_POST = """Na podstawie poniższego posta i informacji o osobie, stwórz e-mail, który ma jak najbardziej zainteresować odbiorcę. E-mail powinien być profesjonalny, przyciągający uwagę, oraz zawierać spersonalizowane odniesienia do treści posta i doświadczenia osoby. E-mail musi również zawierać specjalny link (LINK_TOKEN), który odbiorca powinien kliknąć, a jego konstrukcja powinna maksymalizować prawdopodobieństwo kliknięcia w ten link przez odbiorcę. Dodatkowo, model powinien wymyślić, z jakiej organizacji lub z jakiej potrzeby osoba wysyłająca e-mail pisze, oraz stworzyć wszystkie dane osoby wysyłającej.
 Proszę wygeneruj samego maila, bez żadnych dodatkowych informacji
 W samej treści maila nie odwołuj się do posta na LinkedIN, nie chce aby odbiorca odczuwał, że został stalkowany.

 Treść posta:
 {Treść posta}

 Informacje o osobie:
 {Imię i nazwisko}
 {Organizacja}
 {Rola w organizacji}
 {Zainteresowania/Specjalizacja}

 Odpowiedź:

 TEMAT:
 {temat e-maila z wymyślonymi danymi}

 E-MAIL:
 Drogi/a {Imię},

 {Na początku profesjonalne przedstaw się z wykorzystaniem {wymyślonego imienia i nazwiska}, {wymyślonego tytułu} i {wymyśloną nazwą organizacji}}
 {następnie wymyśl nazwę organizacji oraz jej cel lub potrzeba w kontaktowaniu się/pisania maila}, [Następnie stwórz treść e-maila z odpowiednim wstępem, odniesieniem do treści posta, spersonalizowanym komentarzem związanym z doświadczeniem lub zainteresowaniami osoby, zachętą do kliknięcia w LINK_TOKEN, i zakończeniem zachęcającym do dalszego dialogu.]
 
 {Zakończ e-mail podpisem z wykorzystaniem {wymyślonego imienia i nazwiska}, {wymyślonego tytułu} i {wymyślonej nazwy organizacji}
 EMAIL_TOKEN"""


PROMPT_MAIL_GENERATION_GENERIC = """stwórz e-mail, który ma jak najbardziej zainteresować odbiorcę (imię i nazwisko odbiorcy jest podane). E-mail powinien być profesjonalny, przyciągający uwagę, oraz zawierać spersonalizowane odniesienia do treści posta i doświadczenia osoby. E-mail musi również zawierać specjalny link (LINK_TOKEN), który odbiorca powinien kliknąć, a jego konstrukcja powinna maksymalizować prawdopodobieństwo kliknięcia w ten link przez odbiorcę. Dodatkowo, model powinien wymyślić, z jakiej organizacji lub z jakiej potrzeby osoba wysyłająca e-mail pisze, oraz stworzyć wszystkie dane osoby wysyłającej.
 Proszę wygeneruj samego maila, bez żadnych dodatkowych informacji
 W samej treści maila nie odwołuj się do posta na LinkedIN, nie chce aby odbiorca odczuwał, że został stalkowany.

 Treść posta:
 {Treść posta}

 Informacje o osobie:
 {Imię i nazwisko}
 {Organizacja}
 {Rola w organizacji}
 {Zainteresowania/Specjalizacja}

 Odpowiedź:

 TEMAT:
 {temat e-maila z wymyślonymi danymi}

 E-MAIL:
 Drogi/a {Imię},

 {Na początku profesjonalne przedstaw się z wykorzystaniem {wymyślonego imienia i nazwiska}, {wymyślonego tytułu} i {wymyśloną nazwą organizacji}}
 {następnie wymyśl nazwę organizacji oraz jej cel lub potrzeba w kontaktowaniu się/pisania maila}, [Następnie stwórz treść e-maila z odpowiednim wstępem, odniesieniem do treści posta, spersonalizowanym komentarzem związanym z doświadczeniem lub zainteresowaniami osoby, zachętą do kliknięcia w LINK_TOKEN, i zakończeniem zachęcającym do dalszego dialogu.]
 
 {Zakończ e-mail podpisem z wykorzystaniem {wymyślonego imienia i nazwiska}, {wymyślonego tytułu} i {wymyślonej nazwy organizacji}
 EMAIL_TOKEN"""

 # Function that extracts topic and content of mail
def ExtractEmailParts(emailString) -> [str, str]:
   lines = emailString.split('\n')
   topic = ''
   content = ''
   is_content = False

   for line in lines:
     if line.startswith('TEMAT:'):
       temat = line.replace('TEMAT:', '').strip()
     elif line.startswith('E-MAIL:'):
       is_content = True
     elif is_content:
       content += line.strip() + '\n'

   return topic, content.strip()

# Function returns [mail title, mail content] based on passed context data
def GetMailParams(context: dict[dict[str,str,str,list[str]]], name: str, surname: str) -> [str, str]:
  load_dotenv()

  inputData = f"Imię i Naziwsko osoby do której piszesz maila: `{name}, {surname}`"
  prompt = PROMPT_MAIL_GENERATION_GENERIC
  if 'linkedin' in context:
    if 'organization' in context['linkedin'] and context['linkedin']['organization'] != lss.not_found_str:
      inputData = inputData + f", Organizacja tej osoby: `{context['linkedin']['organization']}`"
    if 'description' in context['linkedin'] and context['linkedin']['description'] != lss.not_found_str:
      inputData = inputData + f", Rola tej osoby: `{context['linkedin']['description']}`"
    if 'posts' in context['linkedin']:
      if len(context['linkedin']['posts']) > 0:
        inputData = inputData + f", Post tej osoby: `{context['linkedin']['posts'][0]}`"
        prompt = PROMPT_MAIL_GENERATION_POST

  client = OpenAI()
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system",
      "content": prompt},
      {"role": "user", "content": inputData}
    ]
  )
  response = completion.choices[0].message.content

  topic, body = ExtractEmailParts(response)

  return [topic, body]
