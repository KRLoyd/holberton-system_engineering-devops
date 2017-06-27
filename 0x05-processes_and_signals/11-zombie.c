#include "zombie.h"
/**
 * main - function to create 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t pid, child_pid, parent_pid;
	unsigned int i;

	pid = 1;

	for (i = 0; i < 5; i++)
	{
		if (pid > 0)
			pid = fork();
		if (pid == 0)
		{
			parent_pid = getppid();
			printf("Parten PID: %d\n", parent_pid);
			child_pid = getpid();
			printf("Zombie process created, PID: %d\n", child_pid);
		}
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
