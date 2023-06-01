/**
 * Author - Debag101
 * Purpose - Average Mark calculator
 * Date - 01 06 2023*/


#include <stdio.h>

// Function to calculate Average marks
float get_average(float mark[], int len) {
	float avg_marks = 0; // Stores Average sum in this var
	for(int i = 0; i < len; i++) 
		avg_marks += mark[i];

	return avg_marks / len; // Returns avg marks
}

// Main exec starts
int main(int argc, char const *argv[]) {
	int student_count;
	// Logger for negative student count
	negative_students:
		printf("\nEnter the number of students in your class => ");
		scanf("%d", &student_count);
		if(student_count < 0) {
			printf("\nPlease enter valid student count !");
			goto negative_students;
		}
	// Getting individual marks in an array
	float marks[student_count];
	for(int i = 0; i < student_count; i++) {
		printf("\nEnter the marks of student %d => ", (i+1));
		scanf("%f", &marks[i]);
	}
	// Printing result
	printf("\nAverage marks of class is %.2f", get_average(marks, student_count));

	
	return 0;
}
