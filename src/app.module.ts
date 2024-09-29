import { Module } from '@nestjs/common';
import { HealthController } from './controllers/health.controller.js';
import { HealthService } from './services/health.service.js';

@Module({
  imports: [],
  controllers: [HealthController],
  providers: [HealthService],
})
// eslint-disable-next-line prettier/prettier
export class AppModule { }
