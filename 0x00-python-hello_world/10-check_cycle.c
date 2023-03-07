#include "lists.h"

/**
 * check_cycle - checks if there is a loop in the linked list
 * @list: the head node passed to us
 * Return: 0 if no loop, 1 if loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		/*if fast and slow pointers meet there is a cycle */
		if (slow == fast)
		{
			return (1);
		}
	}

	/* if fast reaches the end of the list, there is no circle */
	return (0);
}
