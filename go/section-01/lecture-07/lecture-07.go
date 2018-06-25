package main

import (
	"fmt"
	"os"
)

func main() {
	if bytes, error := fmt.Printf("Hello, there!\n"); error != nil {
		os.Exit(1)
	} else if bytes > 5 {
		fmt.Printf("Printed %d bytes \n", bytes)
	}
}
