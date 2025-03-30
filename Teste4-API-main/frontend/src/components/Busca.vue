<template>
  <div class="container">
    <h1>Busca de Operadoras de Saúde</h1>
    <input 
      v-model="termoBusca" 
      @input="buscarEmpresas(true)" 
      placeholder="Digite nome, CNPJ ou cidade..."
      class="search-input"
    />

    <div v-if="carregando" class="carregando">Buscando...</div>

    <div v-if="resultados.length > 0" class="resultados-container">
      <div v-for="empresa in resultados" :key="empresa.CNPJ" class="empresa-item">
        <h2>{{ empresa.Razao_Social }}</h2>
        <p v-if="empresa.Nome_Fantasia"><strong>Nome Fantasia:</strong> {{ empresa.Nome_Fantasia }}</p>
        <p><strong>CNPJ:</strong> {{ empresa.CNPJ }}</p>
        <p><strong>Cidade/UF:</strong> {{ empresa.Cidade }}/{{ empresa.UF }}</p>
        <p><strong>Modalidade:</strong> {{ empresa.Modalidade }}</p>
      </div>

      <!-- Paginação -->
      <div class="paginacao">
        <button @click="mudarPagina(-1)" :disabled="paginaAtual === 1">Anterior</button>
        <span>Página {{ paginaAtual }} de {{ totalPaginas }}</span>
        <button @click="mudarPagina(1)" :disabled="paginaAtual >= totalPaginas">Próxima</button>
      </div>
    </div>
    
    <div v-else-if="termoBusca && !carregando" class="sem-resultados">
      Nenhum resultado encontrado para "{{ termoBusca }}".
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      termoBusca: '',
      resultados: [],
      carregando: false,
      paginaAtual: 1,
      totalPaginas: 1
    };
  },
  methods: {
    buscarEmpresas(resetPagina = false) {
      if (this.termoBusca.length < 3) {
        this.resultados = [];
        this.totalPaginas = 1;
        return;
      }

      if (resetPagina) {
        this.paginaAtual = 1; 
      }

      this.carregando = true;
      axios.get("http://localhost:5000/buscar", {
        params: { 
          termo: this.termoBusca, 
          pagina: this.paginaAtual, 
          tamanho_pagina: 10 
        }
      })
      .then(response => {
        this.resultados = response.data.resultados;
        this.totalPaginas = response.data.total_paginas;
      })
      .catch(error => {
        console.error("Erro na busca:", error);
      })
      .finally(() => {
        this.carregando = false;
      });
    },

    mudarPagina(delta) {
      if (!this.carregando) {
        this.paginaAtual += delta;
        this.buscarEmpresas(false);
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.search-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.carregando {
  color: #2c3e50;
  font-weight: bold;
  margin-bottom: 10px;
}

.resultados-container {
  margin-top: 20px;
}

.empresa-item {
  background-color: #0e0808;
  border-left: 4px solid #2c3e50;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 4px;
}

.paginacao {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.paginacao button {
  padding: 10px;
  border: none;
  background-color: #2c3e50;
  color: white;
  cursor: pointer;
  border-radius: 4px;
}

.paginacao button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
