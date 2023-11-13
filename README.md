# appointment-checker
Appointment checker for German Embassy in Pakistan

## Setup Guide

To host the appointment checker tool remotely, you need SSH access to a machine. This guide will use Digital Ocean (DO), feel free to use any other cloud service provider (e.g, AWS, GCP, etc).

### Fork the repository
1. Click on the fork button in the top right corner of the page to make copy on your GitHub account for your use.

<img width="143" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/f1917d09-fe70-4b4f-8936-3670a0b602bc">

2. Now navigate to your GitHub profile and ensure that you have the repository listed there:

<img width="927" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/b41da1d4-6b03-440d-8091-4cf82de03f17">

### Configure a new GMail account

1. Create a new GMail account. You can skip this step if you already have an account for bot usage.

2. While signed with this account, navigate to this [link](https://myaccount.google.com/).

3. Navigate to the **Security** tab:

<img width="294" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/e51d6d2a-4f52-4683-bd97-62ce1acda67d">

4. Ensure that 2-Step Verification is turned on:

<img width="825" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/3cf5c2e9-4342-4eae-bc7f-ad4ed34ff47a">

5. Once you've configured 2-Step Verification, click on it and you'll be taken to another page. Scroll to the bottom to the **App Passwords** section click on the small arrow next to it.

<img width="731" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/99aac3f1-688d-4a1f-bf25-b21178903e9d">

6. Click on the **Select app** dropdown and click **Other (Custom name)**:

<img width="711" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/dd6e1c7a-3a73-4207-81dd-cde05322af35">

7. Enter an appropriate name and click the **Generate** button:

<img width="720" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/c55c1b69-73a9-4f98-b730-2e4bf06c36c5">

8. Now, copy the password that's in the popup and keep it somewhere safe. You'll have to create a new app password again if you lose this one.

<img width="644" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/4b56bebd-4d6d-47aa-bc58-765e48ec5221">

### Setup the remote machine

1. Sign up on the [DO](https://cloud.digitalocean.com/registrations/new) website. You'll need a working credit/debit card for this step.

> **Note: It would be better if you sign up using your GitHub account. This would save you from the hassle of linking your GitHub account later.**

2. Navigate to the [dashboard](https://cloud.digitalocean.com/).

3. Click on **Apps** under the **Manage** section on the navigation menu left of the page.

<img width="198" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/5604a9ab-123a-4d59-a910-2b56ffece6e2">

4. Press the Create App button and you'll get navigated to the page shown below. Ensure that you have the same configuration as shown in the screenshot below:

<img width="835" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/c070aaa4-b585-4564-be4d-b6f9ad25be7e">

> **Note: In your case, the repository name would be `<your-username>/appointment-checker`**

5. Once you click on **Next**, you'll be navigated to the following page.

<img width="826" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/ccf37bf9-eb94-4a19-84e6-c8230b5d3a72">

6. Ensure that there is only one machine by deleting the second one, as shown below:

<img width="825" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/d5fb9f79-afa5-4c2c-912d-fdfcc19f5cc4">

7. Now, click the **Edit** button on the machine that's left, you'll see the page below:

<img width="831" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/a57d4b4b-1eca-410d-bace-7876c7a3a64d">

8. Edit both **Resource Type** and **Run Command** so that it matches the screenshot below:

<img width="829" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/6ae0d674-ae79-402c-a7c3-42d24f5bf678">

> **Note:** Change the **Command** to `pm2 start main.py --interpreter python3 --no-daemon` as the one in the screenshot breaks.

Once you're done, click on the **Back** button in the bottom left corner.

9. Now, click on the **Edit Plan** button and ensure that you have the following configuraiton:

<img width="825" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/286c6692-c8a0-4ccb-900c-239d469b3f2b">

> **Note: Feel free to use a bigger machine or a Pro machine; however, it would cost accordingly.**

Once you're done, click on the **Back** button in the bottom left corner.

10. Proceed to the subsequent page by clicking on the **Next** button, you'll see the following page:

<img width="826" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/14d58d91-21e9-4c72-9f35-787838afb22e">

11. Now edit the **Global Variables** and add the following variables:

* `SENDER_EMAIL`: The email account through which the script will send the email.
* `SENDER_PASS`: The password for the above email account. If you followed the steps above to create a new GMail account, then you need to use the password that you copied earlier here.
* `RECVR_EMAILS`: List of emails to which the script will notify, space seperated.
* `CHECK_AFTER_SEC`: The number of seconds after which the script should check whether the appointment is open or not (best to keep it at `30` seconds).
* `EMAIL_AFTER_MIN`: Number of minutes after which a status report is to be sent. Best to keep this at `30` minutes to ensure that your mailing qouta doesn't expire for the day.
* `KEYWORD`: The keyword for which the script searches in the appointment options on the webpage. For example, if you want the script to track the Winter intake, then set the value to `winter`.

12. Once done, click on **Next** and you'll be navigated to the Info page:

<img width="830" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/997ab195-f965-4cbc-8a8e-70942bad6c57">

13. Hit **Next** again and eventually click the **Create Resources** button at the bottom of the page:

<img width="563" alt="image" src="https://github.com/drageelr/appointment-checker/assets/56049229/ed4401af-c438-4cf5-a127-186bea3a0ff7">



