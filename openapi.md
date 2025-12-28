# FastAPI
## Version: 0.1.0

### Available authorizations
#### OAuth2PasswordBearer (OAuth2, password)
Token URL: token  
Scopes:

---

### [POST] /register
**Register User**

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [UserCreate](#usercreate)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [User](#user)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

### [POST] /token
**Login For Access Token**

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/x-www-form-urlencoded**: [Body_login_for_access_token_token_post](#body_login_for_access_token_token_post)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [Token](#token)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

---

### [GET] /users/me/
**Read Users Me**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [User](#user)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [PUT] /users/me/language
**Update User**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| language | query |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

---

### [GET] /quizzes
**Get Quizzes**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ [QuizBase](#quizbase) ]<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [GET] /quizzes/search
**Search Quizzes**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| q | query |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ [QuizBase](#quizbase) ]<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [GET] /quizzes/{quiz_id}
**Get Quiz**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| quiz_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [Quiz](#quiz)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [DELETE] /quizzes/{quiz_id}
**Delete Quiz Endpoint**

Delete a quiz and all its associated questions from the server.

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| quiz_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [POST] /quizzes/generate
**Generate Quiz**

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [QuizGenerationRequest](#quizgenerationrequest)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [Quiz](#quiz)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

---

### [GET] /documents
**Get Documents**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ [DocumentCreate](#documentcreate) ]<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [POST] /documents
**Upload Document**

Upload a document (PDF) to the server.

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **multipart/form-data**: [Body_upload_document_documents_post](#body_upload_document_documents_post)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [DocumentCreate](#documentcreate)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [GET] /documents/search
**Search Documents**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| q | query |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ [DocumentCreate](#documentcreate) ]<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [GET] /documents/{doc_id}
**Get Document**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| doc_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [DocumentCreate](#documentcreate)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [DELETE] /documents/{doc_id}
**Delete Document**

Soft delete (disable) a document from the server.

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| doc_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [GET] /documents/{doc_id}/download
**Download Document**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| doc_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [POST] /documents/{doc_id}/summary
**Generate Summary**

Generate a summary for a document using Gemini.
If summary exists in DB, return it.
Otherwise, call Gemini API, save to DB, and return it.

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| doc_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

---

### [GET] /schedule
**Get Schedule**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ [ScheduleInDB](#scheduleindb) ]<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [POST] /schedule
**Create Schedule**

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [Schedule](#schedule)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ScheduleInDB](#scheduleindb)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [GET] /schedule/{schedule_id}
**Get Schedule By Id**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| schedule_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ScheduleInDB](#scheduleindb)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [PUT] /schedule/{schedule_id}
**Update Schedule**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| schedule_id | path |  | Yes | string |

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [Schedule](#schedule)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: [ScheduleInDB](#scheduleindb)<br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

### [DELETE] /schedule/{schedule_id}
**Delete Schedule**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| schedule_id | path |  | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |
| 422 | Validation Error | **application/json**: [HTTPValidationError](#httpvalidationerror)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| OAuth2PasswordBearer |  |

---

### [GET] /health
**Health**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful Response | **application/json**: <br> |

---
### Schemas

#### Body_login_for_access_token_token_post

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| grant_type |  |  | No |
| username | string |  | Yes |
| password | password |  | Yes |
| scope | string |  | No |
| client_id |  |  | No |
| client_secret | undefined (password) |  | No |

#### Body_upload_document_documents_post

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| file | binary |  | Yes |

#### DocumentCreate

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | string |  | Yes |
| filename | string |  | Yes |
| owner | string |  | Yes |
| summary |  |  | No |
| created_at |  |  | No |

#### HTTPValidationError

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| detail | [ [ValidationError](#validationerror) ] |  | No |

#### Quiz

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| quiz_id | string |  | Yes |
| owned_by | string |  | Yes |
| quiz_title | string |  | Yes |
| created_at |  |  | No |
| questions | [ [QuizQuestion](#quizquestion) ] |  | Yes |

#### QuizBase

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| quiz_id | string |  | Yes |
| owned_by | string |  | Yes |
| quiz_title | string |  | Yes |
| created_at |  |  | No |

#### QuizGenerationRequest

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| document_id | string |  | Yes |
| num_questions | integer, <br>**Default:** 10 |  | No |

#### QuizQuestion

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | string |  | Yes |
| question | string |  | Yes |
| options | [ string ] |  | Yes |
| answer_index | integer |  | Yes |
| correct_answer | string |  | Yes |
| why_correct | string |  | Yes |
| created_at |  |  | No |

#### Schedule

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| title | string |  | Yes |
| description | string |  | Yes |
| start_date |  |  | No |
| end_date |  |  | No |

#### ScheduleInDB

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| title | string |  | Yes |
| description | string |  | Yes |
| start_date |  |  | No |
| end_date |  |  | No |
| id | string |  | Yes |
| created_at | integer |  | Yes |
| updated_at | integer |  | Yes |

#### Token

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| access_token | string |  | Yes |
| token_type | string |  | Yes |

#### User

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | Yes |
| email |  |  | No |
| full_name |  |  | No |
| language | string, <br>**Default:** en |  | No |
| created_at |  |  | No |

#### UserCreate

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | Yes |
| email |  |  | No |
| full_name |  |  | No |
| language | string, <br>**Default:** en |  | No |
| password | string |  | Yes |

#### ValidationError

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| loc | [  ] |  | Yes |
| msg | string |  | Yes |
| type | string |  | Yes |
