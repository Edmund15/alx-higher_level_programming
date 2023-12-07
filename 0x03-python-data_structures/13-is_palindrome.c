#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *temp = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        temp = slow;
        slow = slow->next;
        temp->next = prev_slow;
        prev_slow = temp;
    }

    if (fast != NULL)
        slow = slow->next;

    while (prev_slow != NULL && slow != NULL)
    {
        if (prev_slow->n != slow->n)
            return (0);

        prev_slow = prev_slow->next;
        slow = slow->next;
    }

    return (1);
}
