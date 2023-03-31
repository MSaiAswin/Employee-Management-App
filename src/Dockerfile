  FROM ruby:3.0.5
  RUN apt-get update && apt-get install -y nodejs
  WORKDIR /app
  COPY . /app/
  RUN bundle install
  EXPOSE 3000
  CMD ["rails", "server", "-b", "0.0.0.0"]