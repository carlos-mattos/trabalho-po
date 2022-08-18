import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { saveAs } from "file-saver"
import { throwError } from 'rxjs';

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
            return this.httpClient.post(`${this.url}/solve`, data).toPromise();
        } catch (error) {
            console.log(error)
            return null
        }
    }

    downloadPDF(): any {
        var mediaType = 'application/pdf';
        this.httpClient.post(`${this.url}/download-results`, { location: "results.pdf" }, { responseType: 'blob' }).subscribe(
            (response) => {
                var blob = new Blob([response], { type: mediaType });
                saveAs(blob, 'results.pdf');
            },
            e => { throwError(e); }
        );
    }

}