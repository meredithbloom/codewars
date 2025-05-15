using System;
using System.Linq;
using System.Text;

public static class Kata
{
  // 7 KYU - Vowel Count
  public static int GetVowelCount(string str)
  {
    // Your code here
    int vowelCount = 0;
    string vowels = "aeiou";
    foreach (char letter in str) {
      if (vowels.Contains(letter) == true) {
        vowelCount++;
      }
    }
    return vowelCount;
  }

  // 7 KYU - Disembowel Trolls
  public static string Disemvowel(string str)
  {
    string vowels = "aeiouAEIOU";
    var sb = new StringBuilder();
    foreach (char letter in str) {
      if (vowels.Contains(letter) != true) {
        sb.Append(letter);
      }
    }
    return sb.ToString();
  }

  public static bool IsPangram(string str)
  {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    StringBuilder sb = new StringBuilder();
    sb.Append(alphabet);
    foreach (char letter in str.ToLower()) {
      if (alphabet.Contains(letter) == true) {
        sb.Replace(letter.ToString(), "");
      }
    }
    if (sb.ToString().Length == 0) { return true; }
    else { return false; }
  }  
}


// 7 KYU - Mumbling
/*
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt" 
*/
public class Accumul 
{
	public static string Accum(string s) 
  {
    string newStr = "";
    for (int i=0; i<s.Length; i++) {
      char curLetter = s[i];
      int countNeeded = i+1;
      string letterStr = Char.ToUpper(curLetter) + new string(Char.ToLower(curLetter), i);
      if (i < s.Length-1) {
        letterStr+="-";
      }
      newStr+=letterStr;
    }
    return newStr; // your code
  }
}