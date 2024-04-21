using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace HackatonUI
{
    public class TestConfigs
    {
        // Base test interval
        public decimal BaseTestInterval { get; set; }

        // Points for reporting
        public decimal ReportPoints { get; set; }

        // Points for ignoring
        public decimal IgnorePoints { get; set; }

        // Points for failing
        public decimal PenaltyPoints { get; set; }

        // Points limit, users which exceeded the limit shall retake the course
        public decimal PointsThreshold { get; set; }

        // List of departments names
        public List<string> Departments { get; set; }

        // List of test types
        public List<string> TestTypes { get; set; }

        // List of media types
        public List<string> MediaTypes { get; set; }

        [JsonConstructor]
        public TestConfigs(decimal baseTestInterval, decimal reportPoints, 
            decimal ignorePoints, decimal penaltyPoints, decimal pointsThreshold, 
            List<string> departments, List<string> testTypes, List<string> mediaTypes) 
        {
            BaseTestInterval = baseTestInterval;
            ReportPoints = reportPoints;
            IgnorePoints = ignorePoints;
            PenaltyPoints = penaltyPoints;
            PointsThreshold = pointsThreshold;
            Departments = departments;
            TestTypes = testTypes;
            MediaTypes = mediaTypes;
        }
    }
}
