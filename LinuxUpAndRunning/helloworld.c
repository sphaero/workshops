/* helloworld.c
 * ${CROSS_COMPILE}gcc -static helloworld.c -o helloworld
 * */

#include <stdio.h>
#include <unistd.h>
int main(int argc, char *argv[])
{
    printf("Hello world!\n");
    sleep(10);
    printf("Bye world!\n");
}
