import { Injectable } from '@nestjs/common';

@Injectable()
export class HealthService {
  async getHealth(): Promise<string> {
    try {
      const json = JSON.stringify({ message: 'App is healthy !' });
      return JSON.parse(json);
    } catch (error) {
      console.error(error);
      const json = JSON.stringify({ message: 'App is not healthy !' });
      return JSON.parse(json);
    }
  }
}
