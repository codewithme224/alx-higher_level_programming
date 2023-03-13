#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int i = 0, j = 0, k = 0;
    int arr[1000];

    if (*head == NULL)
        return (1);
    while (temp != NULL)
    {
        arr[i] = temp->n;
        temp = temp->next;
        i++;
    }
    i--;
    while (j < i)
    {
        if (arr[j] != arr[i])
            return (0);
        j++;
        i--;
    }
    return (1);
}
