using System;
using System.Text.RegularExpressions;

// Valid Phone Number
// 6 kyu
namespace Kata
{
    public static bool ValidPhoneNumber(string phoneNumber)
    {
        var pattern = @"^\(\d{3}\)\s\d{3}-\d{4}$";
        if (Regex.IsMatch(phoneNumber, pattern))
        {
            Console.WriteLine("Is valid phone number");
            return true;
        }
        Console.WriteLine("Invalid phone number");
        return false;
    }
}