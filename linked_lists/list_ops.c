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

	/* ensure the list is initialized */
	if (list == NULL)
	{
		fprintf(stderr, "The list is not initialized!\n");
		return;
	}

	if (list->size == 0)
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

/**
 * push - adds a node at the beginning of the list
 * @list: the list to insert into
 * @data: the data to insert
 */
void push(list_t *list, int data)
{
	node_t *new_node;

	/* ensure the list is initialized */
	if (list == NULL)
	{
		fprintf(stderr, "The list is not initialized!\n");
		return;
	}

	new_node = malloc(sizeof(node_t));

	if (new_node == NULL)
	{
		fprintf(stderr, "Error: malloc failed. Node insertion failed\n");
		return;
	}

	new_node->data = data;

	if (list->size == 0)
	{
		list->head = new_node;
		list->tail = new_node;
	}
	else
	{
		new_node->next = list->head;
		list->head = new_node;
	}

	list->size++;
}

/**
 * append - adds a node at the end of the list
 * @list: the list to insert into
 * @data: the data to insert
 */
void append(list_t *list, int data)
{
	node_t *new_node;

	/* ensure the list is initialized */
	if (list == NULL)
	{
		fprintf(stderr, "The list is not initialized!\n");
		return;
	}

	new_node = malloc(sizeof(node_t));
	if (new_node == NULL)
	{
		fprintf(stderr, "Error: malloc failed. Node insertion failed\n");
		return;
	}

	new_node->data = data;
	new_node->next = NULL;

	if (list->size == 0)
	{
		list->head = new_node;
		list->tail = new_node;
	}
	else
	{
		list->tail->next = new_node;
		list->tail = new_node;
	}

	list->size++;
}

/**
 * pop - removes an element at the beginning of the linked list
 * @list: the list to remove from
 */
void pop(list_t *list)
{
	node_t *temp;

	if (list->size == 0)
		return;

	temp = list->head;
	list->head = list->head->next;

	free(temp);
	temp = NULL;

	list->size--;

	if (list->size == 0)
	{
		list->head = NULL;
		list->tail = NULL;
	}
}
