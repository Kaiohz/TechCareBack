import { Controller, Get } from '@nestjs/common';
import { HealthService } from '../services/health.service.js';
import { ApiTags } from '@nestjs/swagger';

@ApiTags('health')
@Controller('')
export class HealthController {
  // eslint-disable-next-line prettier/prettier
    constructor(private readonly healthService: HealthService) { }

  @Get('health')
  async getHealth(): Promise<string> {
    return await this.healthService.getHealth();
  }
}
