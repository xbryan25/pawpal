<script setup lang="ts"></script>

<template>
  <section class="h-[90vh] w-[87vw]">
    <div class="flex flex-col">
      <div class="p-5 h-full">
        <h1 class="text-6xl font-semibold">Add Pet</h1>
      </div>

      <div class="flex flex-1 pt-15 px-15 gap-20">
        <div class="flex flex-col gap-4 flex-1">
          <div>
            <h3 class="text-lg font-semibold">Pet Name</h3>
            <label class="dui-input w-full">
              <input maxlength="127" type="text" placeholder="e.g. John" required />
            </label>
          </div>

          <div class="flex gap-4">
            <div class="flex-1">
              <h3 class="text-lg font-semibold">Species</h3>
              <label class="dui-input w-full">
                <input maxlength="127" type="text" placeholder="e.g. John" required />
              </label>
            </div>

            <div class="flex-1">
              <h3 class="text-lg font-semibold">Breed</h3>
              <label class="dui-input w-full">
                <input maxlength="127" type="text" placeholder="e.g. John" required />
              </label>
            </div>
          </div>

          <div class="flex gap-4">
            <div class="flex-1">
              <h3 class="text-lg font-semibold">Sex</h3>
              <label class="dui-input w-full">
                <input maxlength="127" type="text" placeholder="e.g. John" required />
              </label>
            </div>

            <div class="flex-1">
              <h3 class="text-lg font-semibold">Birth Date</h3>
              <input type="date" class="dui-input w-full px-3 py-2" required />
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold">Shelter</h3>
            <label class="dui-input w-full">
              <input maxlength="127" type="text" placeholder="e.g. John" required />
            </label>
          </div>

          <div>
            <h3 class="text-lg font-semibold">Description</h3>
            <textarea class="dui-textarea resize-none w-full" placeholder="Bio"></textarea>
          </div>
        </div>

        <div class="flex flex-col gap-4 flex-1">
          <div>
            <h3 class="text-lg font-semibold">First Photo</h3>
            <div>
              <input
                type="file"
                class="dui-file-input w-full"
                accept="image/png, image/jpeg, image/webp, image/jpg"
              />
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold">Second Photo</h3>
            <div>
              <input
                type="file"
                class="dui-file-input w-full"
                accept="image/png, image/jpeg, image/webp, image/jpg"
              />
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold">Third Photo</h3>
            <div>
              <input
                type="file"
                class="dui-file-input w-full"
                accept="image/png, image/jpeg, image/webp, image/jpg"
              />
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold">Fourth Photo</h3>
            <div>
              <input
                type="file"
                class="dui-file-input w-full"
                accept="image/png, image/jpeg, image/webp, image/jpg"
              />
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold">Fifth Photo</h3>
            <div>
              <input
                type="file"
                class="dui-file-input w-full"
                accept="image/png, image/jpeg, image/webp, image/jpg"
              />
            </div>
          </div>
        </div>
      </div>

      <div class="pt-15 flex justify-center">
        <button class="dui-btn dui-btn-primary w-[15%] text-xl">Create Pet</button>
      </div>
    </div>
  </section>
</template>
