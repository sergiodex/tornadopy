const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
    webpack: function(config, env) {
      config.entry= {
        'index': './src/index.js'
      },
      config.output= {
        filename: '[name].js',
        path: __dirname + '/build'
      }
      config.plugins.push
        new HtmlWebpackPlugin({
          inject: false,
          chunks: ['index'],
          filename: './public/index.html'
        })
      return config;
    },
}