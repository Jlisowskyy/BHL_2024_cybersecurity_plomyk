import DataCollection as dc

# from openai import OpenAI
# from dotenv import load_dotenv


# PROMPT_MAIL_GENERATION = """Na podstawie poniższego posta i informacji o osobie, stwórz e-mail, który będzie jak najbardziej zainteresować odbiorcę. E-mail powinien być profesjonalny, przyciągający uwagę, oraz zawierać spersonalizowane odniesienia do treści posta i doświadczenia osoby. E-mail musi również zawierać specjalny link (LINK_TOKEN), który odbiorca powinien kliknąć, a jego konstrukcja powinna maksymalizować prawdopodobieństwo kliknięcia w ten link przez odbiorcę. Dodatkowo, model powinien wymyślić, z jakiej organizacji lub z jakiej potrzeby osoba wysyłająca e-mail pisze, oraz stworzyć wszystkie dane osoby wysyłającej.
# Proszę wygeneruj samego maila, bez żadnych dodatkowych informacji
# W samej treści maila nie odwołuj się do posta na LinkedIN, nie chce aby odbiorca odczuwał, że został stalkowany.
#
# Treść posta:
# {Treść posta}
#
# Informacje o osobie:
# {Imię i nazwisko}
# {Organizacja}
# {Rola w organizacji}
# {Zainteresowania/Specjalizacja}
#
# Odpowiedź:
#
# TEMAT:
# {temat e-maila z wymyślonymi danymi}
#
# E-MAIL:
# Drogi/a {Imię},
#
# Jestem {Wymyślone imię i nazwisko}, {wymyślony tytuł} w {wymyślona nazwa organizacji}, gdzie zajmujemy się {wymyślony cel lub potrzeba organizacji}. [Treść e-maila z odpowiednim wstępem, odniesieniem do treści posta, spersonalizowanym komentarzem związanym z doświadczeniem lub zainteresowaniami osoby, zachętą do kliknięcia w LINK_TOKEN, i zakończeniem zachęcającym do dalszego dialogu.]
#
# Z poważaniem,
# {Wymyślone imię i nazwisko}
# {Wymyślony tytuł}
# {Wymyślona nazwa organizacji}
# EMAIL_TOKEN"""
#
#
# # Function that extracts topic and content of mail
# def ExtractEmailParts(emailString) -> [str, str]:
#   lines = emailString.split('\n')
#   topic = ''
#   content = ''
#   is_content = False
#
#   for line in lines:
#     if line.startswith('TEMAT:'):
#       temat = line.replace('TEMAT:', '').strip()
#     elif line.startswith('E-MAIL:'):
#       is_content = True
#     elif is_content:
#       content += line.strip() + '\n'
#
#   return topic, content.strip()

# Function returns [mail title, mail content] based on passed context data
def GetMailParams(inputData: str) -> [str, str]:
  # load_dotenv()
  #
  # client = OpenAI()
  # completion = client.chat.completions.create(
  #   model="gpt-3.5-turbo",
  #   messages=[
  #     {"role": "system",
  #      "content": PROMPT_MAIL_GENERATION},
  #     {"role": "user", "content": inputData}
  #   ]
  # )
  # response = completion.choices[0].message.content
  #
  # topic, body = ExtractEmailParts(response)
  #
  # return [topic, body]
  return ["", ""]