using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HackatonUI
{
    public class CompanyInfo
    {
        // Temporary list of depatments, will be replaced with database
        public List<string> departmentNames = new List<string>()
        {
            "Human Resources",
            "Finance and Accounting",
            "Marketing",
            "Sales",
            "Research and Development",
            "Customer Service",
            "Information Technology (IT)",
            "Operations",
            "Administration",
            "Legal and Compliance",
            "Supply Chain Management",
            "Product Management",
            "Quality Assurance",
            "Public Relations",
            "Corporate Communications"
        };

        // Test types list
        public readonly List<string> TestTypes = new List<string>()
        {
            "Attack from the outside",
            "Attack from the inside"
        };

        // Test media list
        public readonly List<string> TestMedia = new List<string>()
        {
            "email",
            "sms"
        };
    }
}
