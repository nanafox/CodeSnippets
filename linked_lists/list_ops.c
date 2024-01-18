#include "list.h"

/**
 * init - initializes a linked list
 *
 * Example:
 *      list_t *my_list = init();
 *
 * Return: the initialized list
 */
list_t *init(void)
{
	list_t *list = malloc(sizeof(list_t));

	if (list == NULL)
	{
		fprintf(stderr, "Error: malloc failed\n");
		exit(EXIT_FAILURE);
	}

	list->head = NULL;
	list->tail = NULL;
	list->size = 0;

	return (list);
}

/**
 * print_list - prints the elements of the linked list
 * @list: the list to print
*/
void print_list(list_t *list)
{
	node_t *tmp;

	if (list == NULL || list->head == NULL)
	{
		printf("Empty list\n");
		return;
	}

	tmp = list->head;
	while (tmp != NULL)
	{
		printf("%d\n", tmp->data);
		tmp = tmp->next;
	}
}
