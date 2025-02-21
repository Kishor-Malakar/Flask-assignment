const axios = require('axios');

const BASE_URL = 'http://127.0.0.1:5000';

describe('Flask API', () => {
    it('should create a new user', async () => {
        const response = await axios.post(`${BASE_URL}/users`, {
            name: 'KishMal',
            email: 'kishmal03@gmail.com'
        });
        expect(response.status).toBe(201);
        expect(response.data.message).toBe('User created successfully');
    });

    it('should get all users', async () => {
        const response = await axios.get(`${BASE_URL}/users`);
        expect(response.status).toBe(200);
        expect(Array.isArray(response.data)).toBe(true);
    });

    it('should get a specific user', async () => {
        const response = await axios.get(`${BASE_URL}/users/1`);
        expect(response.status).toBe(200);
        expect(response.data.id).toBe(1);
        expect(response.data.name).toBe('KishMal');
        expect(response.data.email).toBe('kishmal03@gmail.com');
    });

    it('should update a user', async () => {
        const response = await axios.put(`${BASE_URL}/users/1`, {
            name: 'Jane Doe',
            email: 'jane.doe@example.com'
        });
        expect(response.status).toBe(200);
        expect(response.data.message).toBe('User updated successfully');
    });

    it('should delete a user', async () => {
        const response = await axios.delete(`${BASE_URL}/users/1`);
        expect(response.status).toBe(200);
        expect(response.data.message).toBe('User deleted successfully');
    });
});
