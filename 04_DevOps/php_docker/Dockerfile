# Use the official PHP image with Apache
FROM php:8.2-apache

# Set the working directory inside the container
WORKDIR /var/www/html

# Copy the current directory contents into the container
COPY . .

# Install any PHP extensions if needed (e.g., mysqli, pdo, etc.)
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Expose port 80
EXPOSE 80

# Optional: Set the environment variable for the Apache DocumentRoot
ENV APACHE_DOCUMENT_ROOT /var/www/html/public

# Enable Apache Rewrite Module (if needed)
RUN a2enmod rewrite

# Set the configuration for Apache to use the custom DocumentRoot
COPY ./apache-vhost.conf /etc/apache2/sites-available/000-default.conf