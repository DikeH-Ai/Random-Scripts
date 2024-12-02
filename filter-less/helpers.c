#include "helpers.h"
#include <math.h>
#include <cs50.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
//create a two dimentional loop to update each value
    for (int i = 0, len = height; i < len; i++)
    {
        for (int j = 0, len_width = width; j < len_width; j++)
        {
            int sum = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            int sepia = round(sum / 3.0);
            image[i][j].rgbtBlue = sepia;
            image[i][j].rgbtGreen = sepia;
            image[i][j].rgbtRed = sepia;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
//create a two dimentional loop to update each value
    for (int i = 0; i < (height); i++)
    {
        for (int j = 0; j < (width); j++)
        {
//use the give algorithm to update the pixle's RGB values
            double sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            double sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            double sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            int capped = 255;
//check if each value is within 225 or 8 bits
            if (sepiaRed >= capped)
            {
                sepiaRed = capped;
            }
            image[i][j].rgbtRed = sepiaRed;
            if (sepiaGreen >= capped)
            {
                sepiaGreen = capped;
            }
            image[i][j].rgbtGreen = sepiaGreen;
            if (sepiaBlue >= capped)
            {
                sepiaBlue = capped;
            }
            image[i][j].rgbtBlue = sepiaBlue;


        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //create a two dimentional array
    for (int i = 0; i < height; i++)
    {
        //create a variable count
        int count = 1;
        //create a variable to store the middle position of the width
        int middle = (width / 2);
        //loop through the right half of the width
        for (int j = 0; j < middle; j++)
        {
            //create a variable 'len' that gives us access to the right half of the width
            int len = width - count;
            //swap the values
            RGBTRIPLE image_temp = image[i][j];
            image[i][j] = image[i][len];
            image[i][len] = image_temp;
            //increase count to access the next value from the right half of the width
            count++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //create a copy of image
    RGBTRIPLE image_temp[height][width];
    //variables to derive average of corners, edges and middle pixel
    double count = 9.0;
    double corner = 4.0;
    double edge = 6.0;
    //create a two dimentional array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //copy image to image_temp
            image_temp[i][j] = image[i][j];

        }
    }
    //create a two dimensional array to update image values
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //calculate the average of the left top corner
            if (((i  ==  0) && (j == 0)))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i][j + 1].rgbtRed + image_temp[i + 1][j].rgbtRed +
                                            image_temp[i + 1][j + 1].rgbtRed) / corner);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i][j + 1].rgbtGreen + image_temp[i + 1][j].rgbtGreen +
                                              image_temp[i + 1][j + 1].rgbtGreen) / corner);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i][j + 1].rgbtBlue + image_temp[i + 1][j].rgbtBlue +
                                             image_temp[i + 1][j + 1].rgbtBlue) / corner);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of bottom left corner
            else if ((i == (height - 1)) && (j == 0))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i][j + 1].rgbtRed + image_temp[i - 1][j + 1].rgbtRed +
                                            image_temp[i - 1][j].rgbtRed) / corner);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i][j + 1].rgbtGreen + image_temp[i - 1][j + 1].rgbtGreen +
                                              image_temp[i - 1][j].rgbtGreen) / corner);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i][j + 1].rgbtBlue + image_temp[i - 1][j + 1].rgbtBlue +
                                             image_temp[i - 1][j].rgbtBlue) / corner);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of the top right corner
            else if ((i == 0) && (j == width - 1))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i][j - 1].rgbtRed + image_temp[i + 1][j - 1].rgbtRed +
                                            image_temp[i + 1][j].rgbtRed) / corner);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i][j - 1].rgbtGreen + image_temp[i + 1][j - 1].rgbtGreen +
                                              image_temp[i + 1][j].rgbtGreen) / corner);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i][j - 1].rgbtBlue + image_temp[i + 1][j - 1].rgbtBlue +
                                             image_temp[i + 1][j].rgbtBlue) / corner);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of the bottom right corner
            else if ((i == height - 1) && (j == width - 1))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i][j - 1].rgbtRed + image_temp[i - 1][j - 1].rgbtRed +
                                            image_temp[i - 1][j].rgbtRed) / corner);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i][j - 1].rgbtGreen + image_temp[i - 1][j - 1].rgbtGreen +
                                              image_temp[i - 1][j].rgbtGreen) / corner);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i][j - 1].rgbtBlue + image_temp[i - 1][j - 1].rgbtBlue +
                                             image_temp[i - 1][j].rgbtBlue) / corner);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of top edge
            else if (((i == 0)) && (j != 0 && (j != width - 1)))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i][j + 1].rgbtRed + image_temp[i + 1][j + 1].rgbtRed +
                                            image_temp[i + 1][j].rgbtRed + image_temp[i + 1][j - 1].rgbtRed + image_temp[i][j - 1].rgbtRed) / edge);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i][j + 1].rgbtGreen + image_temp[i + 1][j + 1].rgbtGreen +
                                              image_temp[i + 1][j].rgbtGreen + image_temp[i + 1][j - 1].rgbtGreen + image_temp[i][j - 1].rgbtGreen) / edge);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i][j + 1].rgbtBlue + image_temp[i + 1][j + 1].rgbtBlue +
                                             image_temp[i + 1][j].rgbtBlue + image_temp[i + 1][j - 1].rgbtBlue + image_temp[i][j - 1].rgbtBlue) / edge);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of bottom edge
            else if ((i == height - 1) && (j != 0 && (j != width - 1)))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i][j + 1].rgbtRed + image_temp[i - 1][j + 1].rgbtRed +
                                            image_temp[i - 1][j].rgbtRed + image_temp[i - 1][j - 1].rgbtRed + image_temp[i][j - 1].rgbtRed) / edge);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i][j + 1].rgbtGreen + image_temp[i - 1][j + 1].rgbtGreen +
                                              image_temp[i - 1][j].rgbtGreen + image_temp[i - 1][j - 1].rgbtGreen + image_temp[i][j - 1].rgbtGreen) / edge);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i][j + 1].rgbtBlue + image_temp[i - 1][j + 1].rgbtBlue +
                                             image_temp[i - 1][j].rgbtBlue + image_temp[i - 1][j - 1].rgbtBlue + image_temp[i][j - 1].rgbtBlue) / edge);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }

            //calculate the average of the right edge
            else if ((j == width - 1) && (i != 0 && (i != height - 1)))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i + 1][j].rgbtRed + image_temp[i + 1][j - 1].rgbtRed +
                                            image_temp[i][j - 1].rgbtRed + image_temp[i - 1][j - 1].rgbtRed + image_temp[i - 1][j].rgbtRed) / edge);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i + 1][j].rgbtGreen + image_temp[i + 1][j - 1].rgbtGreen +
                                              image_temp[i][j - 1].rgbtGreen + image_temp[i - 1][j - 1].rgbtGreen + image_temp[i - 1][j].rgbtGreen) / edge);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i + 1][j].rgbtBlue + image_temp[i + 1][j - 1].rgbtBlue +
                                             image_temp[i][j - 1].rgbtBlue + image_temp[i - 1][j - 1].rgbtBlue + image_temp[i - 1][j].rgbtBlue) / edge);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of the left edge
            else if ((j == 0) && (i != 0 && (i != height - 1)))
            {
                double Average_Red = round((image_temp[i][j].rgbtRed + image_temp[i + 1][j].rgbtRed + image_temp[i + 1][j + 1].rgbtRed +
                                            image_temp[i][j + 1].rgbtRed + image_temp[i - 1][j + 1].rgbtRed + image_temp[i - 1][j].rgbtRed) / edge);
                double Average_Green = round((image_temp[i][j].rgbtGreen + image_temp[i + 1][j].rgbtGreen + image_temp[i + 1][j + 1].rgbtGreen +
                                              image_temp[i][j + 1].rgbtGreen + image_temp[i - 1][j + 1].rgbtGreen + image_temp[i - 1][j].rgbtGreen) / edge);
                double Average_Blue = round((image_temp[i][j].rgbtBlue + image_temp[i + 1][j].rgbtBlue + image_temp[i + 1][j + 1].rgbtBlue +
                                             image_temp[i][j + 1].rgbtBlue + image_temp[i - 1][j + 1].rgbtBlue + image_temp[i - 1][j].rgbtBlue) / edge);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;
            }
            //calculate the average of all the pixels within 1 row and 1 column of the original pixel
            else
            {
                double Average_Red = round((image_temp[i - 1][j - 1].rgbtRed + image_temp[i - 1][j].rgbtRed + image_temp[i - 1][j + 1].rgbtRed +
                                            image_temp[i][j - 1].rgbtRed + image_temp[i][j].rgbtRed + image_temp[i][j + 1].rgbtRed +
                                            image_temp[i + 1][j - 1].rgbtRed + image_temp[i + 1][j].rgbtRed + image_temp[i + 1][j + 1].rgbtRed) / count);
                double Average_Green = round((image_temp[i - 1][j - 1].rgbtGreen + image_temp[i - 1][j].rgbtGreen + image_temp[i - 1] [j +
                                              1].rgbtGreen +
                                              image_temp[i][j - 1].rgbtGreen + image_temp[i][j].rgbtGreen + image_temp[i][j + 1].rgbtGreen +
                                              image_temp[i + 1][j - 1].rgbtGreen + image_temp[i + 1][j].rgbtGreen + image_temp[i + 1][j + 1].rgbtGreen) / count);
                double Average_Blue = round((image_temp[i - 1][j - 1].rgbtBlue + image_temp[i - 1][j].rgbtBlue + image_temp[i - 1][j + 1].rgbtBlue +
                                             image_temp[i][j - 1].rgbtBlue + image_temp[i][j].rgbtBlue + image_temp[i][j + 1].rgbtBlue +
                                             image_temp[i + 1][j - 1].rgbtBlue + image_temp[i + 1][j].rgbtBlue + image_temp[i + 1][j + 1].rgbtBlue) / count);
                image[i][j].rgbtRed = Average_Red;
                image[i][j].rgbtGreen = Average_Green;
                image[i][j].rgbtBlue = Average_Blue;

            }

        }
    }
    return;
}

