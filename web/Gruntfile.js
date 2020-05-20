// ### in Gruntfile.js ###
module.exports = function(grunt){
    require('load-grunt-tasks')(grunt);
    grunt.initConfig({
        watch: {
            livereload: {
                tasks: ['clean', 'browserify'],
                options: {
                    livereload: true
                },
                files: [
                    './public/**/*.less',
                    './public/**/*.jsx',
                    './public/**/*.js',
                    './views/**/*.ejs'
                ]
          }
        }, // End watch

        nodemon: {
            dev: {
                options: {
                    nodeArgs: ['--debug'],
                    file: '--debug ./bin/www'
                }
            }
        }, //End nodemon

        concurrent: {
            dev: {
                options: {
                    logConcurrentOutput: true
                },
                tasks: ['watch', 'nodemon:dev']
            }
        }, // End concurrent

        clean: {
            build: {
                src: ['./public/javascripts/build.min.js']
            }
        }, // End clean

        browserify: {
            options: {
                transform: [ require('grunt-react').browserify ]
            },
            files: {
                src: ['./public/javascripts/**/*.jsx', './public/javascripts/**/*.js'],
                dest: './public/javascripts/build.min.js'
            }
        } // End browserify
    });

    grunt.registerTask('default', ['clean', 'browserify', 'concurrent:dev']);
};