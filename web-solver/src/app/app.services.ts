import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface IVariables {
    x1: number
    x2: number
}

@Injectable({
    providedIn: 'root'
})
export class SolverService {

    url = 'http://localhost:3001';

    constructor(private httpClient: HttpClient) { }

    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    }

    solveProblem({ x1, x2 }: IVariables) {
        try {
            return this.httpClient.post(`${this.url}/test`, { x1, x2 }).toPromise()
        } catch (error) {
            console.log(error)
            return null
        }
    }

}