#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct node_s - blueprint for a singly linked list
 * @data: the data portion
 * @next: the pointer to the next node
 */
typedef struct node_s
{
	int data;
	struct node_s *next;
} node_t;

/**
 * struct list_s - a blueprint for a linked list
 * @head: a pointer to the head node
 * @tail: a pointer to the tail node
 * @size: the size (length) of the linked list
 */
typedef struct list_s
{
	node_t *head;
	node_t *tail;
	size_t size;
} list_t;

#define first(list) (list->head->data)
#define last(list) (list->tail->data)

/* function prototypes */

list_t *init(void);
void append(list_t *list, int data);
void push(list_t *list, int data);
void pop(list_t *list);
void print_list(list_t *list);
void print_element_at(list_t *list, int index);

#endif /* LIST_H */
