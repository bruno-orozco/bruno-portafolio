new Vue({
    el: '#app',

    delimiters: ['[[', ']]'],

    data() {
        return {
        saludo : "Hola",

        color: "#f4f4f4",
    
        show: false,

        input: 500000, 

        objetivo_mes: 6000000,

        porciento: 100,

        }
    },

    computed: {
        tasa_avance () {
            return ((this.input * this.porciento) / this.objetivo_mes).toFixed(2);
        },
        commaInput () {
            return (this.input).toLocaleString('es-MX',  {minimumFractionDigits: 0, maximumFractionDigits: 2})
        },
        commaObjMes () {
            return (this.objetivo_mes).toLocaleString('es-MX',  {minimumFractionDigits: 0, maximumFractionDigits: 2})
        },
        objetivo_dia () {
            const ultimoDia = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0).getDate();

            const primerDia = new Date(new Date()).getDate() -1;

            return ((this.objetivo_mes - this.input) / (ultimoDia - primerDia)).toLocaleString('es-MX', {minimumFractionDigits: 0, maximumFractionDigits: 2});
        },
        
    },

    methods: {
        mostrarTexto () {
            this.show = !this.show
        }
    }
})