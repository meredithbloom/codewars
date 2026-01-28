using System;

public namespace Kata
{
    // Buying a car
    // 6 kyu
    public class BuyCar
    {
        // [number of months to save up money to buy new car, how much money leftover]
        // nbMonths(2000, 8000, 1000, 1.5) // returns [6, 766]
        public static int[] nbMonths(int startPriceOld, int startPriceNew, int savingPerMonth, double percentLossByMonth)
        {
            double oldPrice = (double)startPriceOld;
            double newPrice = (double)startPriceNew;
            var monthCounter = 0;
            var savedMoney = 0;
            while ((oldPrice - newPrice) + savedMoney < 0)
            {
                monthCounter++;
                Console.WriteLine($"Start of month {monthCounter}, value of old car={oldPrice}, value of new car={newPrice}, savings={savedMoney}, current % loss={percentLossByMonth}");
                if (monthCounter != 0 && monthCounter % 2 == 0)
                {
                Console.WriteLine($"Current percent loss per month {percentLossByMonth} increasing...");
                percentLossByMonth += .5;
                }
                oldPrice -= oldPrice * (percentLossByMonth / 100);
                newPrice -= newPrice * (percentLossByMonth / 100);
                savedMoney += savingPerMonth;
                var leftover = (oldPrice - newPrice) + savedMoney;
                Console.WriteLine($"End of month {monthCounter}: percent_loss {percentLossByMonth}, available: {leftover}");
            }
            int roundedDifference = Convert.ToInt32((oldPrice - newPrice) + savedMoney);
            Console.WriteLine($"{monthCounter}, {roundedDifference}");
            return [monthCounter, roundedDifference];
        }
    }
}

