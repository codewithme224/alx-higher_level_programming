#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	/* Allocate memory for the new node*/
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	/* Initialize the new node*/
	new_node->val = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->val)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}


	listint_t *current = *head;

	while (current->next != NULL && number >= current->next->val)
	{
		current = current->next;
	}

	/* Insert the new node into the list*/
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
