import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { setupSwagger } from './swagger';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  setupSwagger(app, 'Auth Service');
  await app.listen(process.env.PORT ?? 3001, '0.0.0.0');
}
bootstrap();
