# credit_card
credit card validator app using the Luhn algorithm.
python libraries used: tkinter, random

On a credit card, a checksum is a single digit in the account number that allows a computer, or anyone familiar with the formula involved, to determine whether the number is valid. The checksum can help identify credit card numbers that have been entered incorrectly -- or phony credit card numbers created by counterfeiters.

The Algorithm in Action

Verifying a 16-digit card number starts by taking the first 15 digits, which are the institution code and the individual account identifier. For example, in the card number 4578 4230 1376 9219, those digits would be:
4-5-7-8-4-2-3-0-1-3-7-6-9-2-1
Starting with the first digit, multiply every second digit by 2:
8-5-14-8-8-2-6-0-2-3-14-6-18-2-2
Every time you have a two-digit number, just add those digits together for a one-digit result:
8-5-5-8-8-2-6-0-2-3-5-6-9-2-2
Finally, add all the numbers together:
8 + 5 + 5 + 8 + 8 + 2 + 6 + 0 + 2 + 3 + 5 + 6 + 9 + 2 + 2 = 71
When this number is added to the check digit, then the result must be an even multiple of 10. In this case:
71 + 9 = 80
The number is therefore valid. If the algorithm doesn't produce a multiple of 10, then the card number cannot be valid.

![Screenshot 2021-09-02 at 17 26 47](https://user-images.githubusercontent.com/76489213/131864464-f7b3603e-2912-4552-aae2-fca6bd0fc041.png)
![Screenshot 2021-09-02 at 17 27 19](https://user-images.githubusercontent.com/76489213/131864496-4a3ab744-1e7f-484a-b94f-93c69a476d8a.png)
![Screenshot 2021-09-02 at 17 27 47](https://user-images.githubusercontent.com/76489213/131864523-4e11c3ef-3d1b-4241-a1ae-587a20511c3c.png)
![Screenshot 2021-09-02 at 17 29 02](https://user-images.githubusercontent.com/76489213/131864549-3588d744-3433-4595-803e-0be39406f896.png)


