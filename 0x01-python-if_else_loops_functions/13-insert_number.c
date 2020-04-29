#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
* insert_node - function
* @head: beginning of list
* @number: number to insert
*
* Description: Function to insert a number to a sorted list
* Return: address of new node, or NULL if Fail
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;

	temp = *head;
	if (head == NULL)
		return (NULL);
	temp = malloc(sizeof(int));
	if (temp == NULL)
		return (NULL);
	if (number == 0)
		return (0);
	return (0);
}
