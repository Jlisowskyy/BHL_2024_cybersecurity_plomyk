namespace HackatonUI
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            tableLayoutPanel1 = new TableLayoutPanel();
            SetupTable = new TableLayoutPanel();
            IntervalPanel = new Panel();
            IntervalLabel = new Label();
            IntervalNumericUpDown = new NumericUpDown();
            ReportPointsPanel = new Panel();
            ReportPointsLabel = new Label();
            ReportPointsNumericUpDown = new NumericUpDown();
            IgnorePointsPanel = new Panel();
            IgnorePointsLabel = new Label();
            IgnorePointsNumericUpDown = new NumericUpDown();
            PenaltyPointsPanel = new Panel();
            PenaltyPointsLabel = new Label();
            PenaltyPointsNumericUpDown = new NumericUpDown();
            PointsThresholdPanel = new Panel();
            PointsThreshold = new Label();
            PointsThresholdNumericUpDown = new NumericUpDown();
            ConfigButtonsPanel = new Panel();
            SendButton = new Button();
            button1 = new Button();
            SaveConfigButton = new Button();
            RightTable = new TableLayoutPanel();
            TestTypeLabel = new Label();
            TestTypeLayout = new FlowLayoutPanel();
            TestMediaLabel = new Label();
            TestMediaLayout = new FlowLayoutPanel();
            LeftTable = new TableLayoutPanel();
            DepartmentsLayout = new FlowLayoutPanel();
            DepartmentsLabel = new Label();
            tableLayoutPanel1.SuspendLayout();
            SetupTable.SuspendLayout();
            IntervalPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)IntervalNumericUpDown).BeginInit();
            ReportPointsPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)ReportPointsNumericUpDown).BeginInit();
            IgnorePointsPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)IgnorePointsNumericUpDown).BeginInit();
            PenaltyPointsPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)PenaltyPointsNumericUpDown).BeginInit();
            PointsThresholdPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)PointsThresholdNumericUpDown).BeginInit();
            ConfigButtonsPanel.SuspendLayout();
            RightTable.SuspendLayout();
            LeftTable.SuspendLayout();
            SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.ColumnCount = 3;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 34.0564F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 37.4186554F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 28.5249462F));
            tableLayoutPanel1.Controls.Add(SetupTable, 1, 0);
            tableLayoutPanel1.Controls.Add(RightTable, 2, 0);
            tableLayoutPanel1.Controls.Add(LeftTable, 0, 0);
            tableLayoutPanel1.Dock = DockStyle.Fill;
            tableLayoutPanel1.Location = new Point(0, 0);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 1;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            tableLayoutPanel1.Size = new Size(922, 453);
            tableLayoutPanel1.TabIndex = 0;
            // 
            // SetupTable
            // 
            SetupTable.ColumnCount = 1;
            SetupTable.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            SetupTable.Controls.Add(IntervalPanel, 0, 0);
            SetupTable.Controls.Add(ReportPointsPanel, 0, 1);
            SetupTable.Controls.Add(IgnorePointsPanel, 0, 2);
            SetupTable.Controls.Add(PenaltyPointsPanel, 0, 3);
            SetupTable.Controls.Add(PointsThresholdPanel, 0, 4);
            SetupTable.Controls.Add(ConfigButtonsPanel, 0, 5);
            SetupTable.Dock = DockStyle.Fill;
            SetupTable.Location = new Point(317, 3);
            SetupTable.Name = "SetupTable";
            SetupTable.RowCount = 6;
            SetupTable.RowStyles.Add(new RowStyle(SizeType.Percent, 16F));
            SetupTable.RowStyles.Add(new RowStyle(SizeType.Percent, 16F));
            SetupTable.RowStyles.Add(new RowStyle(SizeType.Percent, 16F));
            SetupTable.RowStyles.Add(new RowStyle(SizeType.Percent, 16F));
            SetupTable.RowStyles.Add(new RowStyle(SizeType.Percent, 16F));
            SetupTable.RowStyles.Add(new RowStyle(SizeType.Percent, 20F));
            SetupTable.Size = new Size(339, 447);
            SetupTable.TabIndex = 3;
            // 
            // IntervalPanel
            // 
            IntervalPanel.BackColor = SystemColors.Control;
            IntervalPanel.Controls.Add(IntervalLabel);
            IntervalPanel.Controls.Add(IntervalNumericUpDown);
            IntervalPanel.Dock = DockStyle.Fill;
            IntervalPanel.Location = new Point(3, 3);
            IntervalPanel.Name = "IntervalPanel";
            IntervalPanel.Size = new Size(333, 65);
            IntervalPanel.TabIndex = 0;
            // 
            // IntervalLabel
            // 
            IntervalLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            IntervalLabel.AutoSize = true;
            IntervalLabel.Location = new Point(0, 0);
            IntervalLabel.Name = "IntervalLabel";
            IntervalLabel.Size = new Size(195, 20);
            IntervalLabel.TabIndex = 1;
            IntervalLabel.Text = "Phishing test interval in days";
            // 
            // IntervalNumericUpDown
            // 
            IntervalNumericUpDown.Location = new Point(0, 23);
            IntervalNumericUpDown.Minimum = new decimal(new int[] { 100, 0, 0, int.MinValue });
            IntervalNumericUpDown.Name = "IntervalNumericUpDown";
            IntervalNumericUpDown.Size = new Size(320, 27);
            IntervalNumericUpDown.TabIndex = 0;
            // 
            // ReportPointsPanel
            // 
            ReportPointsPanel.Controls.Add(ReportPointsLabel);
            ReportPointsPanel.Controls.Add(ReportPointsNumericUpDown);
            ReportPointsPanel.Dock = DockStyle.Fill;
            ReportPointsPanel.Location = new Point(3, 74);
            ReportPointsPanel.Name = "ReportPointsPanel";
            ReportPointsPanel.Size = new Size(333, 65);
            ReportPointsPanel.TabIndex = 1;
            // 
            // ReportPointsLabel
            // 
            ReportPointsLabel.AutoSize = true;
            ReportPointsLabel.Location = new Point(0, 0);
            ReportPointsLabel.Name = "ReportPointsLabel";
            ReportPointsLabel.Size = new Size(279, 20);
            ReportPointsLabel.TabIndex = 2;
            ReportPointsLabel.Text = "Points for reporting the phishing attempt";
            // 
            // ReportPointsNumericUpDown
            // 
            ReportPointsNumericUpDown.Location = new Point(0, 23);
            ReportPointsNumericUpDown.Name = "ReportPointsNumericUpDown";
            ReportPointsNumericUpDown.Size = new Size(320, 27);
            ReportPointsNumericUpDown.TabIndex = 3;
            // 
            // IgnorePointsPanel
            // 
            IgnorePointsPanel.Controls.Add(IgnorePointsLabel);
            IgnorePointsPanel.Controls.Add(IgnorePointsNumericUpDown);
            IgnorePointsPanel.Dock = DockStyle.Fill;
            IgnorePointsPanel.Location = new Point(3, 145);
            IgnorePointsPanel.Name = "IgnorePointsPanel";
            IgnorePointsPanel.Size = new Size(333, 65);
            IgnorePointsPanel.TabIndex = 2;
            // 
            // IgnorePointsLabel
            // 
            IgnorePointsLabel.AutoSize = true;
            IgnorePointsLabel.Location = new Point(0, 0);
            IgnorePointsLabel.Name = "IgnorePointsLabel";
            IgnorePointsLabel.Size = new Size(270, 20);
            IgnorePointsLabel.TabIndex = 4;
            IgnorePointsLabel.Text = "Points for ignoring thr phishing attempt";
            // 
            // IgnorePointsNumericUpDown
            // 
            IgnorePointsNumericUpDown.Location = new Point(0, 23);
            IgnorePointsNumericUpDown.Name = "IgnorePointsNumericUpDown";
            IgnorePointsNumericUpDown.Size = new Size(320, 27);
            IgnorePointsNumericUpDown.TabIndex = 5;
            // 
            // PenaltyPointsPanel
            // 
            PenaltyPointsPanel.Controls.Add(PenaltyPointsLabel);
            PenaltyPointsPanel.Controls.Add(PenaltyPointsNumericUpDown);
            PenaltyPointsPanel.Dock = DockStyle.Fill;
            PenaltyPointsPanel.Location = new Point(3, 216);
            PenaltyPointsPanel.Name = "PenaltyPointsPanel";
            PenaltyPointsPanel.Size = new Size(333, 65);
            PenaltyPointsPanel.TabIndex = 3;
            // 
            // PenaltyPointsLabel
            // 
            PenaltyPointsLabel.AutoSize = true;
            PenaltyPointsLabel.Location = new Point(0, 0);
            PenaltyPointsLabel.Name = "PenaltyPointsLabel";
            PenaltyPointsLabel.Size = new Size(186, 20);
            PenaltyPointsLabel.TabIndex = 6;
            PenaltyPointsLabel.Text = "Points for failing in the test";
            // 
            // PenaltyPointsNumericUpDown
            // 
            PenaltyPointsNumericUpDown.Location = new Point(0, 23);
            PenaltyPointsNumericUpDown.Name = "PenaltyPointsNumericUpDown";
            PenaltyPointsNumericUpDown.Size = new Size(320, 27);
            PenaltyPointsNumericUpDown.TabIndex = 7;
            // 
            // PointsThresholdPanel
            // 
            PointsThresholdPanel.Controls.Add(PointsThreshold);
            PointsThresholdPanel.Controls.Add(PointsThresholdNumericUpDown);
            PointsThresholdPanel.Dock = DockStyle.Fill;
            PointsThresholdPanel.Location = new Point(3, 287);
            PointsThresholdPanel.Name = "PointsThresholdPanel";
            PointsThresholdPanel.Size = new Size(333, 65);
            PointsThresholdPanel.TabIndex = 4;
            // 
            // PointsThreshold
            // 
            PointsThreshold.AutoSize = true;
            PointsThreshold.Location = new Point(0, 0);
            PointsThreshold.Name = "PointsThreshold";
            PointsThreshold.Size = new Size(114, 20);
            PointsThreshold.TabIndex = 9;
            PointsThreshold.Text = "Points threshold";
            // 
            // PointsThresholdNumericUpDown
            // 
            PointsThresholdNumericUpDown.Location = new Point(0, 23);
            PointsThresholdNumericUpDown.Name = "PointsThresholdNumericUpDown";
            PointsThresholdNumericUpDown.Size = new Size(320, 27);
            PointsThresholdNumericUpDown.TabIndex = 10;
            // 
            // ConfigButtonsPanel
            // 
            ConfigButtonsPanel.Controls.Add(SendButton);
            ConfigButtonsPanel.Controls.Add(button1);
            ConfigButtonsPanel.Controls.Add(SaveConfigButton);
            ConfigButtonsPanel.Dock = DockStyle.Fill;
            ConfigButtonsPanel.Location = new Point(3, 358);
            ConfigButtonsPanel.Name = "ConfigButtonsPanel";
            ConfigButtonsPanel.Size = new Size(333, 86);
            ConfigButtonsPanel.TabIndex = 5;
            // 
            // SendButton
            // 
            SendButton.Location = new Point(0, 38);
            SendButton.Name = "SendButton";
            SendButton.Size = new Size(326, 29);
            SendButton.TabIndex = 10;
            SendButton.Text = "Send";
            SendButton.UseVisualStyleBackColor = true;
            SendButton.Click += SendButton_Click;
            // 
            // button1
            // 
            button1.Location = new Point(166, 3);
            button1.Name = "button1";
            button1.Size = new Size(160, 29);
            button1.TabIndex = 9;
            button1.Text = "Load config";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // SaveConfigButton
            // 
            SaveConfigButton.Location = new Point(0, 3);
            SaveConfigButton.Name = "SaveConfigButton";
            SaveConfigButton.Size = new Size(160, 29);
            SaveConfigButton.TabIndex = 8;
            SaveConfigButton.Text = "Save config";
            SaveConfigButton.UseVisualStyleBackColor = true;
            SaveConfigButton.Click += SaveConfigButton_Click;
            // 
            // RightTable
            // 
            RightTable.ColumnCount = 1;
            RightTable.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            RightTable.Controls.Add(TestTypeLabel, 0, 0);
            RightTable.Controls.Add(TestTypeLayout, 0, 1);
            RightTable.Controls.Add(TestMediaLabel, 0, 2);
            RightTable.Controls.Add(TestMediaLayout, 0, 3);
            RightTable.Dock = DockStyle.Fill;
            RightTable.Location = new Point(662, 3);
            RightTable.Name = "RightTable";
            RightTable.RowCount = 4;
            RightTable.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            RightTable.RowStyles.Add(new RowStyle(SizeType.Absolute, 70F));
            RightTable.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            RightTable.RowStyles.Add(new RowStyle(SizeType.Absolute, 200F));
            RightTable.Size = new Size(257, 447);
            RightTable.TabIndex = 4;
            // 
            // TestTypeLabel
            // 
            TestTypeLabel.AutoSize = true;
            TestTypeLabel.Location = new Point(3, 0);
            TestTypeLabel.Name = "TestTypeLabel";
            TestTypeLabel.Size = new Size(68, 20);
            TestTypeLabel.TabIndex = 0;
            TestTypeLabel.Text = "Test type";
            // 
            // TestTypeLayout
            // 
            TestTypeLayout.Dock = DockStyle.Fill;
            TestTypeLayout.Location = new Point(3, 23);
            TestTypeLayout.Name = "TestTypeLayout";
            TestTypeLayout.Size = new Size(251, 64);
            TestTypeLayout.TabIndex = 1;
            // 
            // TestMediaLabel
            // 
            TestMediaLabel.AutoSize = true;
            TestMediaLabel.Location = new Point(3, 90);
            TestMediaLabel.Name = "TestMediaLabel";
            TestMediaLabel.Size = new Size(81, 20);
            TestMediaLabel.TabIndex = 2;
            TestMediaLabel.Text = "Test media";
            // 
            // TestMediaLayout
            // 
            TestMediaLayout.Dock = DockStyle.Top;
            TestMediaLayout.Location = new Point(3, 113);
            TestMediaLayout.Name = "TestMediaLayout";
            TestMediaLayout.Size = new Size(251, 125);
            TestMediaLayout.TabIndex = 3;
            // 
            // LeftTable
            // 
            LeftTable.ColumnCount = 1;
            LeftTable.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            LeftTable.Controls.Add(DepartmentsLayout, 0, 1);
            LeftTable.Controls.Add(DepartmentsLabel, 0, 0);
            LeftTable.Dock = DockStyle.Fill;
            LeftTable.Location = new Point(3, 3);
            LeftTable.Name = "LeftTable";
            LeftTable.RowCount = 2;
            LeftTable.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            LeftTable.RowStyles.Add(new RowStyle());
            LeftTable.Size = new Size(308, 447);
            LeftTable.TabIndex = 5;
            // 
            // DepartmentsLayout
            // 
            DepartmentsLayout.AutoScroll = true;
            DepartmentsLayout.Dock = DockStyle.Fill;
            DepartmentsLayout.Location = new Point(3, 23);
            DepartmentsLayout.Name = "DepartmentsLayout";
            DepartmentsLayout.Size = new Size(302, 421);
            DepartmentsLayout.TabIndex = 0;
            // 
            // DepartmentsLabel
            // 
            DepartmentsLabel.AutoSize = true;
            DepartmentsLabel.Location = new Point(3, 0);
            DepartmentsLabel.Name = "DepartmentsLabel";
            DepartmentsLabel.Size = new Size(95, 20);
            DepartmentsLabel.TabIndex = 1;
            DepartmentsLabel.Text = "Departments";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(922, 453);
            Controls.Add(tableLayoutPanel1);
            MaximumSize = new Size(940, 500);
            MinimumSize = new Size(940, 500);
            Name = "Form1";
            Text = "Form1";
            tableLayoutPanel1.ResumeLayout(false);
            SetupTable.ResumeLayout(false);
            IntervalPanel.ResumeLayout(false);
            IntervalPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)IntervalNumericUpDown).EndInit();
            ReportPointsPanel.ResumeLayout(false);
            ReportPointsPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)ReportPointsNumericUpDown).EndInit();
            IgnorePointsPanel.ResumeLayout(false);
            IgnorePointsPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)IgnorePointsNumericUpDown).EndInit();
            PenaltyPointsPanel.ResumeLayout(false);
            PenaltyPointsPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)PenaltyPointsNumericUpDown).EndInit();
            PointsThresholdPanel.ResumeLayout(false);
            PointsThresholdPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)PointsThresholdNumericUpDown).EndInit();
            ConfigButtonsPanel.ResumeLayout(false);
            RightTable.ResumeLayout(false);
            RightTable.PerformLayout();
            LeftTable.ResumeLayout(false);
            LeftTable.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private TableLayoutPanel tableLayoutPanel1;
        private NumericUpDown IntervalNumericUpDown;
        private Label IntervalLabel;
        private NumericUpDown IgnorePointsNumericUpDown;
        private Label IgnorePointsLabel;
        private NumericUpDown ReportPointsNumericUpDown;
        private Label ReportPointsLabel;
        private NumericUpDown PenaltyPointsNumericUpDown;
        private Label PenaltyPointsLabel;
        private Button SaveConfigButton;
        private Label PointsThreshold;
        private NumericUpDown PointsThresholdNumericUpDown;
        private TableLayoutPanel SetupTable;
        private Panel IntervalPanel;
        private Panel ReportPointsPanel;
        private Panel IgnorePointsPanel;
        private Panel PenaltyPointsPanel;
        private Panel PointsThresholdPanel;
        private Panel ConfigButtonsPanel;
        private Button button1;
        private TableLayoutPanel RightTable;
        private Label TestTypeLabel;
        private FlowLayoutPanel TestTypeLayout;
        private Label TestMediaLabel;
        private FlowLayoutPanel TestMediaLayout;
        private TableLayoutPanel LeftTable;
        private FlowLayoutPanel DepartmentsLayout;
        private Label DepartmentsLabel;
        private Button SendButton;
    }
}
