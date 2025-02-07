# SwiftShopBot (WITH SENSITIVE DATA REPLACED BY "---")

## Overview

SwiftShopBot is an automated bot developed for testing the functionality and operations of an internal online shop (company-internal). It simulates the entire purchasing flow, including logging into user accounts, selecting items, adding them to the cart, proceeding with checkout, confirming orders, and canceling orders. The bot also sends notifications to a Microsoft Teams channel for important events such as successful order cancellations.

This bot is designed for testing and operational management purposes to ensure smooth shopping experiences, identify issues with the checkout process, and verify the functionality of various features across user accounts.

## Key Features

- **Simulate User Interactions:** Automates the process of logging in, adding items to the cart, selecting sizes, checking out, and canceling orders.
- **Customizable Item Selection:** Selects random items for purchase from predefined URLs for testing.
- **Order Management:** Includes functionality to confirm and cancel orders.
- **Microsoft Teams Notifications:** Sends real-time notifications to a Microsoft Teams webhook regarding critical events (order confirmation, cancellation).
- **Email Account Management:** Utilizes a list of email accounts stored in a text file to simulate multiple user logins.

## Prerequisites

To run this bot, you need to have the following installed:

- **Python 3.7+**
- **Selenium** for browser automation  
- **PyAutoGUI** for mouse automation  
- **Requests** for sending HTTP requests to Microsoft Teams  
- **Microsoft Edge WebDriver** (matching the installed version of Edge)

## Safety and Usage Guidelines

- **Testing Environment Only:**  
  This bot is designed to be used in a controlled, internal testing environment. It should **not** be used on live production websites unless explicitly intended and authorized.

- **Rate Limiting and Anti-Abuse:**  
  The bot performs multiple actions (logins, purchases, cancellations) in rapid succession. Be sure to set up any necessary rate limiting and avoid using it excessively on live platforms.

- **Legal Compliance:**  
  Always ensure that you have the proper permissions to use automated scripts like this on any web platform.
