using System.Data;
using System.Diagnostics;
using System.Text.Json;

namespace HackatonUI
{
    public partial class Form1 : Form
    {
        // Temporary list of dtrings for each department
        private CompanyInfo _companyInfo;
        private Process _interpreter;
        
        public Form1()
        {
            InitializeComponent();
            Closed += CloseInterpreter;

            _companyInfo = new CompanyInfo();

            BootupInterpreter();
            
            InitPanels();
            InitUpDowns();
        }


        private void BootupInterpreter()
        {
            var currentPath = Environment.CurrentDirectory;
            string parentDirectory = Path.GetDirectoryName(currentPath);
            string resPath = Path.Combine(parentDirectory, "ConnectionSolution");
            Environment.CurrentDirectory = resPath;
            Console.WriteLine(Environment.CurrentDirectory);

            _interpreter = new Process();
            _interpreter.StartInfo.FileName = "C:\\Users\\Jlisowskyy\\AppData\\Local\\Programs\\Python\\Python312\\python.exe";
            _interpreter.StartInfo.UseShellExecute = false;
            _interpreter.StartInfo.Arguments = "Application.py";
            _interpreter.StartInfo.RedirectStandardOutput = true;
            _interpreter.StartInfo.RedirectStandardInput = true;
            _interpreter.StartInfo.RedirectStandardError = true;
            _interpreter.StartInfo.CreateNoWindow = true;
            _interpreter.Start();

            BootupProcedure(_interpreter.StandardOutput);
        }

        private void BootupProcedure(StreamReader interpreterRead)
        {
            var line = interpreterRead.ReadLine();
            if (line == null)
                return;

            var departments = line.Split(',', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
            _companyInfo.departmentNames = [..departments];
            interpreterRead.Close();
        }
        
        private void CloseInterpreter(object? sender, EventArgs e)
        {
            _interpreter.StandardInput.WriteLine("exit");
            // _interpreter.Kill();
            _interpreter.Dispose();
        }
        
        private void UpdateDepartments()
        {
            var streamWrite = _interpreter.StandardInput;
            streamWrite.WriteLine($"upt {PrepareConfig()}");
        }

        // Initialization of the list of departments
        private void InitPanels()
        {
            foreach (string departmentName in _companyInfo.departmentNames)
            {
                CheckBox checkBox = new CheckBox();
                checkBox.Text = departmentName;
                checkBox.Width = DepartmentsLayout.Width;
                DepartmentsLayout.Controls.Add(checkBox);
            }

            foreach (string testType in _companyInfo.TestTypes)
            {
                CheckBox checkBox = new CheckBox();
                checkBox.Text = testType;
                checkBox.Width = TestTypeLayout.Width;
                TestTypeLayout.Controls.Add(checkBox);
            }

            foreach (string testMedia in _companyInfo.TestMedia)
            {
                CheckBox checkBox = new CheckBox();
                checkBox.Text = testMedia;
                checkBox.Width = TestMediaLayout.Width;
                TestMediaLayout.Controls.Add(checkBox);
            }
        }

        // Initializing updowns limits and base value
        private void InitUpDowns()
        {
            IntervalNumericUpDown.Minimum = 1;
            IntervalNumericUpDown.Maximum = int.MaxValue;
            IntervalNumericUpDown.Value = 7;

            IgnorePointsNumericUpDown.Minimum = int.MinValue;
            IgnorePointsNumericUpDown.Maximum = int.MaxValue;
            IgnorePointsNumericUpDown.Value = -5;

            PenaltyPointsNumericUpDown.Minimum = int.MinValue;
            PenaltyPointsNumericUpDown.Maximum = int.MaxValue;
            PenaltyPointsNumericUpDown.Value = -10;

            ReportPointsNumericUpDown.Minimum = int.MinValue;
            ReportPointsNumericUpDown.Maximum = int.MaxValue;
            ReportPointsNumericUpDown.Value = 5;

            PointsThresholdNumericUpDown.Minimum = int.MinValue;
            PointsThresholdNumericUpDown.Maximum = int.MaxValue;
            PointsThresholdNumericUpDown.Value = -20;
        }

        // Prepare config
        private string PrepareConfig()
        {
            List<string> checkedDepartments = new List<string>();
            foreach (var control in DepartmentsLayout.Controls)
            {
                var checkbox = control as CheckBox;
                if (checkbox!.Checked == true)
                    checkedDepartments.Add(checkbox!.Text);
            }

            List<string> checkedTestTypes = new List<string>();
            foreach (var control in TestTypeLayout.Controls)
            {
                var checkbox = control as CheckBox;
                if (checkbox!.Checked == true)
                    checkedTestTypes.Add(checkbox!.Text);
            }

            List<string> checkedMediaTypes = new List<string>();
            foreach (var control in TestMediaLayout.Controls)
            {
                var checkbox = control as CheckBox;
                if (checkbox!.Checked == true)
                    checkedMediaTypes.Add(checkbox!.Text);
            }

            TestConfigs testConfigs = new TestConfigs(
                IntervalNumericUpDown.Value,
                ReportPointsNumericUpDown.Value,
                IgnorePointsNumericUpDown.Value,
                PenaltyPointsNumericUpDown.Value,
                PointsThresholdNumericUpDown.Value,
                checkedDepartments,
                checkedTestTypes,
                checkedMediaTypes);

            string config = JsonSerializer.Serialize(testConfigs);
            return config;
        }

        // Saving config
        private void SaveConfig()
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.InitialDirectory = "c:\\";
                openFileDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    // Get the path of specified file
                    var filePath = openFileDialog.FileName;
                    var config = PrepareConfig();

                    using (var writer = new StreamWriter(filePath))
                    {
                        writer.WriteLine(config);
                    }
                }
            }
        }

        private void LoadConfig()
        {
            string config = "";
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                // openfiledialog setup
                openFileDialog.InitialDirectory = "c:\\";
                openFileDialog.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    // Get the path of specified file
                    var filePath = openFileDialog.FileName;
                    config = "";

                    using (var reader = new StreamReader(filePath))
                    {
                        config = reader.ReadToEnd();
                    }
                }
            }

            // deserialization
            TestConfigs? testConfigs = JsonSerializer.Deserialize<TestConfigs>(config);

            if (testConfigs == null)
                return;

            SetUp(testConfigs);
        }

        private void SetUp(TestConfigs testConfigs)
        {
            IntervalNumericUpDown.Value = testConfigs.BaseTestInterval;
            IgnorePointsNumericUpDown.Value = testConfigs.IgnorePoints;
            PenaltyPointsNumericUpDown.Value = testConfigs.PenaltyPoints;
            ReportPointsNumericUpDown.Value = testConfigs.ReportPoints;
            PointsThresholdNumericUpDown.Value = testConfigs.PointsThreshold;

            HashSet<string> dpNames = new HashSet<string>();
            foreach (var dp in testConfigs.Departments)
            {
                dpNames.Add(dp);
            }

            HashSet<string> testNames = new HashSet<string>();
            foreach (var testName in testConfigs.TestTypes)
            {
                testNames.Add(testName);
            }

            HashSet<string> testMedia = new HashSet<string>();
            foreach (var mediaType in testConfigs.MediaTypes)
            {
                testMedia.Add(mediaType);
            }

            foreach (var control in DepartmentsLayout.Controls)
            {
                var checkbox = control as CheckBox;
                if (dpNames.Contains(checkbox!.Text))
                    checkbox.Checked = true;
                else
                    checkbox.Checked = false;
            }

            foreach (var control in TestTypeLayout.Controls)
            {
                var checkbox = control as CheckBox;
                if (testNames.Contains(checkbox!.Text))
                    checkbox.Checked = true;
                else
                    checkbox.Checked = false;
            }

            foreach (var control in TestMediaLayout.Controls)
            {
                var checkbox = control as CheckBox;
                if (testMedia.Contains(checkbox!.Text))
                    checkbox.Checked = true;
                else
                    checkbox.Checked = false;
            }
        }

        private void SaveConfigButton_Click(object sender, EventArgs e)
        {
            SaveConfig();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            LoadConfig();
        }

        private void SendButton_Click(object sender, EventArgs e)
        {
            UpdateDepartments();
        }
    }
}
