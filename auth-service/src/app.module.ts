import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UserModule } from './user/user.module';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'db',
      port: 5432,
      username: 'user',
      password: 'password',
      database: 'restaurant',
      autoLoadEntities: true, // Automatically load all entities
      synchronize: true, // ⚠️ Auto-migrate (use only in dev)
    }),
    UserModule, // Import User module
  ],
})
export class AppModule {}
