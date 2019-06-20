using System;

namespace CodeProjects
{
    class Program
    {
        static void Main(string[] args) //Given an array of integers, return a new array such that each element of index i of the new array 
                                        //is the product of all the numbers in the original array except the one at i
                                        // DCP #2 [HARD] Uber With and Without Divison
        {
            int[] input = { 1, 2, 3, 4 };


            //WITH DIVISION
            int[] output = new int[input.Length];
            int PROD = 1;
            for (int i=1; i < input.Length+1; i++) //Creates a product of all the elements in the input array
            {
                PROD = PROD * input[i-1];
                Console.WriteLine(input[i-1]);
            }
            for (int i=0; i < input.Length; i++)
            {
                output[i] = PROD / input[i]; //For each element in output, divides out the corresponding input element. Leaving a product of the other elements.
                Console.WriteLine(output[i]);
            }

            //WITHOUT DIVISION
            int[] output2 = new int[input.Length];

            for (int i=0; i < input.Length; i++)
            {
                output2[i] = 1; //Doesn't properly deal with arrays of length 1!
                
                for (int j=0; j< input.Length; j++)
                { 
                    if (i!=j)
                    {
                        //Multiply by each element that is not i (j).
                        output2[i] = output2[i] * input[j];
                    }                 
                }
                Console.WriteLine(output2[i]);
            }




            return;
        }
    }
}
