<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;

Route::post('/login', [AuthController::class, 'login']);

Route::group(['middleware' => 'auth:api'], function () {
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::get('/me', [AuthController::class, 'me']);

    Route::get('/dados-protegidos', function () {
        return response()->json([
            'mensagem' => 'Acesso liberado via JWT!',
            'dados' => 'Simulando resposta de alta carga'
        ]);
    });
});
