import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class SolverService {

    url = 'http://localhost:3001';

    constructor(private httpClient: HttpClient) { }

    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'multipart/form-data', 'Accept': 'application/json' })
    }

    solveProblem(data: FormData) {
        try {
            return this.httpClient.post(`${this.url}/test`, data).toPromise()
        } catch (error) {
            console.log(error)
            return null
        }
    }

}