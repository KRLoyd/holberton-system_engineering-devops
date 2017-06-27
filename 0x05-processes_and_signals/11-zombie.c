#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int infinite_while(void);
/**
 * main - function to create 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - function to make main sleep forever
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
