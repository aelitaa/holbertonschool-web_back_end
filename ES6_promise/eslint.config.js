const globals = require('globals');
const jestPlugin = require('eslint-plugin-jest');
const airbnbBase = require('eslint-config-airbnb-base');

module.exports = [
  {
    files: ['*.js'],
    excludedFiles: ['babel.config.js'],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        ...globals.es6,
        ...globals.jest,
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
      },
    },
    plugins: {
      jest: jestPlugin,
    },
    extends: [
      'airbnb-base',
      'plugin:jest/all',
    ],
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
    linterOptions: {
      reportUnusedDisableDirectives: true,
    },
  },
  {
    ignores: ['babel.config.js'],
  },
  {
    ignores: ['node_modules/**'],
  },
];

