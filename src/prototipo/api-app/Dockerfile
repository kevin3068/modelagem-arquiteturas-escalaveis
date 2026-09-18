# Usa a imagem oficial do PHP com o servidor Apache integrado
FROM php:8.4.2-apache

# Instala as dependências do sistema e extensões do PHP necessárias para o Laravel
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    curl

# Instala as extensões essenciais para comunicação com o banco e operações do Laravel
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Habilita o mod_rewrite do Apache (necessário para o roteamento do Laravel)
RUN a2enmod rewrite

# Configura o diretório raiz do Apache para apontar para a pasta public do Laravel
ENV APACHE_DOCUMENT_ROOT /var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Define o diretório de trabalho padrão
WORKDIR /var/www/html

# Copia os arquivos do projeto para o contêiner
COPY . .

# Ajusta as permissões das pastas que o Laravel precisa escrever (logs, cache, etc)
# Em ambiente local, o '|| true' previne erros se as pastas ainda não existirem
RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache || true
