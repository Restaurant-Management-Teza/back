import { INestApplication } from '@nestjs/common';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

/**
 * Set up Swagger documentation for the given application.
 * @param app - The NestJS application instance
 * @param serviceName - The name of the microservice (for Swagger title)
 */
export function setupSwagger(app: INestApplication, serviceName: string): void {
  // Swagger Configuration
  const config = new DocumentBuilder()
    .setTitle(`${serviceName} API`)
    .setDescription(`API documentation for the ${serviceName}`)
    .setVersion('1.0')
    .addBearerAuth() // Optional: for JWT auth if needed
    .build();

  // Create Swagger document
  const document = SwaggerModule.createDocument(app, config);

  // Serve Swagger UI at /api/docs
  SwaggerModule.setup('api/docs', app, document);

  console.log(`✅ Swagger for ${serviceName} available at /api/docs`);
}
