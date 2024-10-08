include <stdlib.h>
#include <stdio.h>
#define BUFSIZE 10

int main(int argc, char **argv) {
	FILE *fp;
	char scurr[BUFSIZE];
	long new, curr, incr, min = 10;

	/* An argument with an integer increment must be supplied */
	if (argc != 2 || (incr = strtol(argv[1], NULL, 10)) == 0) { return(1); }
	if ((fp = fopen("/sys/class/backlight/ideapad/brightness", "r+")) && fgets(scurr, BUFSIZE, fp)) {
		curr = strtol(scurr, NULL, 10);
		rewind(fp);
		new = curr + incr;
		if (new < min) { new = min; }
		fprintf(fp, "%ld\n", new);
		fclose(fp);
	} else { return(2); }
	return(0);
}
