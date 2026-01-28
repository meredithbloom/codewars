using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;

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

  // 6 KYU - Detect Pangram
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

  // 6 KYU - Who likes it?
  /*
  []                                -->  "no one likes this"
  ["Peter"]                         -->  "Peter likes this"
  ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
  ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
  ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
  */
  public static string Likes(string[] name)
  {
    string nameStr;
    int nameCount = name.Length;
    switch (nameCount)
    {
      case 1:
        nameStr = $"{name[0]} likes this";
        break;
      case 2:
        nameStr = $"{name[0]} and {name[1]} like this";
        break;
      case 3:
        nameStr = $"{name[0]}, {name[1]} and {name[2]} like this";
        break;
      case >= 4:
        nameStr = $"{name[0]}, {name[1]} and {nameCount-2} others like this";
        break;
      default:
        nameStr = "no one likes this";
        break;
    }
    return nameStr; 
  }

  // 6 KYU - Duplicate Encoder
  /*
  The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

  "din"      =>  "((("
  "recede"   =>  "()()()"
  "Success"  =>  ")())())"
  "(( @"     =>  "))((" 
  */
  public static string DuplicateEncode(string word)
  {
    word = word.ToLower();
    List<string> charList = new List<string>();
    foreach (char character in word) {
      if (word.Count(l => l == character) == 1) {
        charList.Add("(");
      } else {
        charList.Add(")");
      }
    }
    return string.Concat(charList);
  }

  // 5 KYU - First non-repeating character
  // If a string has no unique characters, it should return an empty string
  public static string FirstNonRepeatingLetter(string s)
  {
    string copy = s.ToLower();
    foreach (char letter in s) {
      char lowerCase = char.ToLower(letter);
      if (copy.Count(x => x == lowerCase) == 1) {
        return letter.ToString();
      }
    }
    return "";
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