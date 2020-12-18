  

var app1 = new Vue({
  el: '#app-1',
  data: {
    customers: [],
    seen:true,
    unseen:false
  },

  created: function() {
    this.fetchChartData();
    this.timer = setInterval(this.fetchChartData,60000);
  },
  methods: {
    fetchChartData: function() {
      axios
        .get('/Data_Visualization/')
        .then(response => (this.customers = response.data.customers))
        console.log(this.customers)
    },
    cancelAutoUpdate: function() {clearInterval(this.timer)}
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  }
})

