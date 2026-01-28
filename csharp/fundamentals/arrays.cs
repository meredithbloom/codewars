using System;
using System.Linq;
using System.Collections.Generic;

public class Kata
{
    // Equal sides of an array - 6kyu
    public static int FindEvenIndex(int[] arr)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            var firstPart = arr[0..i];
            var secondPart = arr[(i+1)..];
            var firstSum = firstPart.Sum();
            var secondSum = secondPart.Sum();
            if (firstSum == secondSum)
            {
                return i;
            }
        }
        return -1;
    }

    // The Supermarket Queue - 6 kyu
    // int[] customers - representing amount of time each customer needs to check out (in order)
    // int n - number of self checkout tills
    public static long QueueTime(int[] customers, int n)
    {
        // only ONE queue serving many tills
        // list to track total time accumulated at each till
        var tills = new List<long>(new long[n]);
        if (n == 1)
        {
            return customers.Sum();
        }
        else
        {

        }
        return totalTime;
    }

    // queueTime([5,3,4], 1)
    // should return 12
    // because when there is 1 till, the total time is just the sum of the times

    // queueTime([10,2,3,3], 2)
    // should return 10
    // because here n=2 and the 2nd, 3rd, and 4th people in the 
    // queue finish before the 1st person has finished.

    // queueTime([2,3,10], 2)
    // should return 12
}

