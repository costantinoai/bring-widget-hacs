import resolve from '@rollup/plugin-node-resolve';
import typescript from '@rollup/plugin-typescript';
import terser from '@rollup/plugin-terser';

const dev = process.env.ROLLUP_WATCH;

export default {
  input: 'src/bring-shopping-card.ts',
  output: {
    file: 'dist/bring-shopping-card.js',
    format: 'es',
    sourcemap: dev ? true : false,
  },
  plugins: [
    resolve(),
    typescript(),
    !dev && terser({
      format: {
        comments: false,
      },
    }),
  ].filter(Boolean),
};
