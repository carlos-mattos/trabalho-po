import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class CarService {

    url = 'http://localhost:3001';

    constructor(private httpClient: HttpClient) { }

    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    }

    getCars() {
        try {
            this.httpClient.get(`${this.url}/test`).subscribe(result => console.log(result))

        } catch (error) {
            console.log(error)
        }
    }

}