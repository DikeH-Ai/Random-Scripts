#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //check for one command
    if (argc > 2)
    {
        printf("Error, ONLY ONE COMMAND ALLOWED\n");
        return 1;
    }
    //open the memory card
    FILE *fptr = fopen(argv[1], "r");
    //check if the memory card exist
    if (fptr == NULL)
    {
        printf("Error, INVALID FILE\n");
        return 1;
    }
    //block size variable
    int block_size = 512;
    //sprintf array
    char newname[9];
    //buffer array of type BYTE and size block_size
    BYTE buffer[block_size];
    //counter
    int count = 0;
    //file pointer
    FILE *pfile;
    //checking process for each 512 block of memory
    while (fread(buffer, 1, block_size, fptr) == block_size)
    {
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count == 0)
            {
                sprintf(newname, "%03i.jpg", count);
                pfile = fopen(newname, "a+");
                fwrite(buffer, 1, block_size, pfile);
                count++;
            }
            else if (count > 0)
            {

                fclose(pfile);
                sprintf(newname, "%03i.jpg", count);
                pfile = fopen(newname, "a+");
                fwrite(buffer, 1, block_size, pfile);
                count++;
            }

        }
        else if (count > 0)
        {
            fwrite(buffer, 1, block_size, pfile);
        }
    }
    //close files
    fclose(pfile);
    fclose(fptr);
}
